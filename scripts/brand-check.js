// The brand layer (docs/stylesheets/extra.css, overrides/main.html) restates three Material
// assumptions that break on a mkdocs-material upgrade. This runs in the page and returns the
// three readings as JSON: the active nav link width (0 or tiny = the search float collapsed it),
// the number of search results for a typed query and whether the results panel is visible, and
// every rendered colour that is not neutral (R==G==B) or the brand yellow. Compare the readings
// from a build on the old version with those from the new one; they should match.
// See README.md, "After a Material upgrade".
(async()=>{
 const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 const act=document.querySelector('.md-nav__link--active')||document.querySelector('.md-nav__link');
 const navW=act?Math.round(act.getBoundingClientRect().width):-1;
 const inp=document.querySelector('.md-search__input');
 let results=-1, resVisible=false;
 if(inp){ inp.focus(); inp.value='playlist'; inp.dispatchEvent(new Event('input',{bubbles:true})); inp.dispatchEvent(new KeyboardEvent('keyup',{bubbles:true})); await sleep(1500);
   const items=[...document.querySelectorAll('.md-search-result__item')]; results=items.length;
   const out=document.querySelector('.md-search__output'); if(out){const r=out.getBoundingClientRect(); const cs=getComputedStyle(out); resVisible=r.height>0&&cs.visibility!=='hidden'&&cs.opacity!=='0';}
 }
 const ok=new Set(['rgb(236, 255, 12)','rgba(236, 255, 12, 1)']); const odd=new Set();
 for(const e of document.querySelectorAll('body *')){ const cs=getComputedStyle(e); if(cs.display==='none'||cs.visibility==='hidden') continue;
   for(const k of ['color','backgroundColor','borderTopColor','borderBottomColor','borderLeftColor','borderRightColor']){ const v=cs[k]; const m=v.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/); if(!m) continue; if(m[4]==='0') continue; const [r,g,b]=[+m[1],+m[2],+m[3]]; if(r===g&&g===b) continue; if(ok.has(v)) continue; odd.add(v+' on '+e.tagName.toLowerCase()+(e.className&&typeof e.className==='string'?'.'+e.className.split(' ')[0]:'')); } }
 return JSON.stringify({navW,results,resVisible,odd:[...odd].slice(0,12)});
})()
