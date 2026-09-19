#target indesign
(function(){
var base=File($.fileName).parent, name='human-park-1-gesamt-rohsatz-r006.indd';
var doc=app.documents.itemByName(name);
if(!doc.isValid)doc=app.open(File(base.parent.fsName+'/'+name));
function quote(s){return '"'+String(s).replace(/"/g,'""')+'"';}
var rows=['text_id,physical_position,page_label,native_story_id,text'],seen={};
for(var p=0;p<doc.pages.length;p++){
 var frames=doc.pages[p].textFrames;
 for(var i=0;i<frames.length;i++){
  var t=frames[i],id=t.label;
  if(id.indexOf('PAGE-NUMBER-')==0)continue;
  if(!id)throw Error('Unlabeled text frame on physical page '+(p+1));
  if(seen[id])throw Error('Duplicate text ID '+id);seen[id]=true;
  if(t.parentStory.textContainers.length!=1)throw Error('Threaded story requires explicit mapping: '+id);
  rows.push([quote(id),p+1,quote(doc.pages[p].label),quote(t.parentStory.id),quote(t.parentStory.contents)].join(','));
 }
}
var f=File(base.fsName+'/native-texts.csv');f.encoding='UTF-8';f.lineFeed='Unix';f.open('w');f.write(rows.join('\n')+'\n');f.close();
var m=File(base.fsName+'/export-status.txt');m.encoding='UTF-8';m.open('w');m.write('document='+doc.fullName.fsName+'\nunsaved_changes='+doc.modified+'\ntext_frames='+(rows.length-1)+'\nexported_at='+new Date().toUTCString()+'\n');m.close();
})();
