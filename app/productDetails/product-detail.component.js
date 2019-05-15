  'use strict';

// Register `phoneDetail` component, along with its associated controller and template
angular.
  module('productDetail').
  component('productDetail', {
    templateUrl: 'productDetails/product-detail.template.html',
    controller: ['$http', '$routeParams',
      function PhoneDetailController($http, $routeParams) {
        var self = this;

        self.setImage = function setImage(imageUrl) {
          self.mainImageUrl = imageUrl;
        };

        $http.get('products/' + $routeParams.productId + '.json').then(function(response) {
          self.product = response.data;
          self.setImage(self.product.images[0]);
        });
      }
    ]
  });