"""Free-tier cautious The Odds API connector; never fabricates probability or Tippmix odds."""
import datetime as dt
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

UTC=dt.timezone.utc
NOW=dt.datetime.now(UTC)
KEY=os.environ.get('ODDS_API_KEY','').strip()
OUT=Path('data/live.json')

def get(url):
    req=Request(url,headers={'Accept':'application/json','User-Agent':'TippmixPro/4.1'})
    with urlopen(req,timeout=25) as response:
        data=response.read(2_000_001)
        if len(data)>2_000_000:raise ValueError('API response too large')
        return json.loads(data),dict(response.headers)

def iso(value):
    if not isinstance(value,str):return None
    try:
        d=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
        return d.astimezone(UTC) if d.tzinfo else None
    except ValueError:return None

def main():
    if not KEY:
        print('ODDS_API_KEY is not set; no update.');return
    root='https://api.the-odds-api.com/v4/sports/'
    sports,_=get(root+'?'+urlencode({'apiKey':KEY}))
    if not isinstance(sports,list):raise ValueError('Invalid sports response')
    # Up to 5 leagues per run, free plan: one market and one region = ~1 credit per league.
    # Soccer leagues prioritized, plus at most one tennis and one darts key if available.
    soccer_priority=['soccer_epl','soccer_germany_bundesliga','soccer_italy_serie_a']
    keys={s.get('key'):s for s in sports if isinstance(s,dict) and s.get('active')}
    chosen=[k for k in soccer_priority if k in keys]
    for prefix in ('tennis_','darts_'):
        candidates=sorted(k for k in keys if k.startswith(prefix))
        if candidates:chosen.append(candidates[0])
    chosen=chosen[:5]
    if not chosen:
        print('No supported active sports; leaving feed unchanged');return
    results=[];spent=0;remaining=None
    for key in chosen:
        url=root+key+'/odds/?'+urlencode({'apiKey':KEY,'regions':'eu','markets':'h2h','oddsFormat':'decimal'})
        data,headers=get(url)
        if not isinstance(data,list):continue
        try:spent+=int(headers.get('x-requests-last','0'))
        except ValueError:pass
        try:remaining=int(headers.get('x-requests-remaining','0'))
        except ValueError:pass
        sport='Labdarúgás' if key.startswith('soccer_') else 'Tenisz' if key.startswith('tennis_') else 'Darts'
        for event in data:
            if not isinstance(event,dict):continue
            kickoff=iso(event.get('commence_time'))
            if not kickoff or not NOW<kickoff<NOW+dt.timedelta(days=10):continue
            home=event.get('home_team');away=event.get('away_team')
            if not isinstance(home,str) or not isinstance(away,str) or not home or not away:continue
            for book in event.get('bookmakers',[])[:15]:
                if not isinstance(book,dict):continue
                for market in book.get('markets',[]):
                    if not isinstance(market,dict) or market.get('key')!='h2h':continue
                    checked=iso(market.get('last_update'))
                    if not checked or not NOW-dt.timedelta(hours=12)<=checked<=NOW+dt.timedelta(minutes=5):continue
                    for outcome in market.get('outcomes',[]):
                        if not isinstance(outcome,dict):continue
                        price=outcome.get('price');name=outcome.get('name')
                        if not isinstance(price,(float,int)) or not 1<price<=100 or not isinstance(name,str):continue
                        results.append({'sport':sport,'match':f'{home} – {away}'[:200],
                            'market':('Győztes: '+name)[:200], 'odds':float(price),
                            'source':('The Odds API / '+str(book.get('title','unknown'))+' (nem Tippmix)')[:200],
                            'checked':checked.isoformat(),'kickoff':kickoff.isoformat()})
    # Retain only fresh future events; no made-up odds and no probabilities.
    results.sort(key=lambda e:(e['kickoff'],e['match'],e['market']))
    results=results[:300]
    if remaining is not None and remaining<10:print('Warning: odds API credits nearly exhausted')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({'updated_at':NOW.isoformat(),'events':results,'source':'The Odds API',
        'quota_spent_this_run':spent,'quota_remaining':remaining,'sports_checked':chosen},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Saved',len(results),'markets; credits used',spent,'remaining',remaining)

if __name__=='__main__':main()
