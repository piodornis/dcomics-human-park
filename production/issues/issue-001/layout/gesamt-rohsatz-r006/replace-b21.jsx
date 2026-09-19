#target indesign
(function(){
var base=File($.fileName).parent,src=app.documents.itemByName('human-park-1-gesamt-rohsatz-r005.indd');
if(!src.isValid)src=app.open(File(base.parent.fsName+'/heft-1-gesamt-rohsatz-r005/human-park-1-gesamt-rohsatz-r005.indd'));
var ui=app.scriptPreferences.userInteractionLevel;app.scriptPreferences.userInteractionLevel=UserInteractionLevels.NEVER_INTERACT;
try{
var f=File(base.fsName+'/human-park-1-gesamt-rohsatz-r006.indd');src.saveACopy(f);var doc=app.open(f),count=0;
for(var i=0;i<doc.links.length;i++){
 var link=doc.links[i],name=link.name;
 if(name=='s013-p04.png'){name='s013-p04-b21.png';count++;}
 if(name=='s013-p05.png'){name='s013-p05-b21.png';count++;}
 link.relink(File(base.fsName+'/artwork/'+name));link.update();
 if(name=='s013-p04-b21.png'||name=='s013-p05-b21.png'){
  var fr=link.parent.parent;fr.fit(FitOptions.FILL_PROPORTIONALLY);fr.fit(FitOptions.CENTER_CONTENT);
 }
}
if(count!=2)throw Error('Expected two replaced panels; found '+count);
doc.recompose();for(var i=0;i<doc.textFrames.length;i++)if(doc.textFrames[i].overflows)throw Error('Overflow '+doc.textFrames[i].label);
for(var i=0;i<doc.links.length;i++)if(doc.links[i].status!=LinkStatus.NORMAL)throw Error('Bad link '+doc.links[i].name);
doc.insertLabel('HP_REVISION','gesamt-r006');doc.save();doc.exportFile(ExportFormat.INDESIGN_MARKUP,File(base.fsName+'/human-park-1-gesamt-rohsatz-r006.idml'));
app.pdfExportPreferences.pageRange=PageRange.ALL_PAGES;app.pdfExportPreferences.exportReaderSpreads=false;app.pdfExportPreferences.useDocumentBleedWithPDF=false;
doc.exportFile(ExportFormat.PDF_TYPE,File(base.fsName+'/human-park-1-lesefassung-r006.pdf'));
}finally{app.scriptPreferences.userInteractionLevel=ui;}
})();
