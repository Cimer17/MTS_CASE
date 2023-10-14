ymaps.ready(function () {
  var myMap = new ymaps.Map(
      "map",
      {
        center: [56.362509, 41.31093], // Ковров
        zoom: 13,
        controls: ["zoomControl"], // Добавление элемента управления масштабом
      },
      {
        searchControlProvider: "yandex#search",
      }
    ),
    objectManager = new ymaps.ObjectManager({
      clusterize: true,
      gridSize: 32,
      clusterDisableClickZoom: true,
    });

  // Чтобы задать опции одиночным объектам и кластерам,
  // обратимся к дочерним коллекциям ObjectManager.
  objectManager.objects.options.set("preset", "islands#greenDotIcon");
  objectManager.clusters.options.set("preset", "islands#greenClusterIcons");
  myMap.geoObjects.add(objectManager);

  // Загрузка данных из JSON-файла и создание меток
  $.ajax({
    url: "static/data.json",
  }).done(function (data) {
    // Модификация данных: добавление кастомных изображений
    data.features.forEach(function (feature) {
      feature.options = {
        iconLayout: "default#image",
        iconImageHref: feature.properties.iconImageHref, // Путь к изображению метки из JSON
        iconImageSize: [30, 30],
        iconImageOffset: [-15, -15],
      };
    });

    objectManager.add(data);
  });
});
