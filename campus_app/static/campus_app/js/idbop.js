var dbPromise = idb.open('campus-app-db', 1, function(upgradeDb) {
 upgradeDb.createObjectStore('noticia',{keyPath:'pk'});
});

fetch('http://127.0.0.1:8000/getdata').then(function(response){
  return response.json();
}).then(function(jsondata){
    dbPromise.then(function(db){
      var tx = db.transaction('noticia', 'readwrite');
      var feedsStore = tx.objectStore('noticia');
      for(var key in jsondata){
        if (jsondata.hasOwnProperty(key)) {
          feedsStore.put(jsondata[key]);
        }
      }
    });
  });

var post = "";
dbPromise.then(function(db){
  var tx = db.transaction('noticia', 'readonly');
  var feedsStore = tx.objectStore('noticia');
  return feedsStore.openCursor();
}).then(function logItems(cursor) {
    if (!cursor) {
      document.getElementById('offlinedata').innerHTML=post;
      return;
    }
    for (var field in cursor.value) {
      if(field == 'fields'){
        feedsData=cursor.value[field];
        for(var key in feedsData){
          if(key =='titulo'){
            var titulo = '<h3>'+feedsData[key]+'</h3>';
          }
          if(key =='texto'){
            var texto = feedsData[key];
          }
          if(key == 'prioridade'){
            var prioridade = '<p>'+feedsData[key]+'</p>';
          }
        }
        post=post+'<br>'+titulo+'<br>'+texto+'<br>'+prioridade+'<br>';
      }
    }
    return cursor.continue().then(logItems);
  });