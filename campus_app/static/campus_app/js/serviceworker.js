// Set this to true for production.
var doCache = true;

// Name of our cache.
var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  if (doCache) {
    event.waitUntil(
      caches.open(staticCacheName).then(function (cache) {
        return cache.addAll([
          '/base_layout'
        ]);
      })
    );
  }
});

self.addEventListener('fetch', function(event) {
  if (doCache) {
    var requestUrl = new URL(event.request.url);
      if (requestUrl.origin === location.origin) {
        if ((requestUrl.pathname === '/')) {
          event.respondWith(caches.match('/base_layout'));
          return;
        }
      }
      event.respondWith(
        caches.match(event.request).then(function(response) {
          return response || fetch(event.request);
        })
      );
  }
});