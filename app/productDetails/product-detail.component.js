  'use strict';

// Register `phoneDetail` component, along with its associated controller and template
/*angular.
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
  });*/



  
  angular.
  module('productDetail').
  component('productDetail', {
   templateUrl: 'productDetails/product-detail.template.html',
    controller: ['$q','$http','$routeParams',
      function ProductDetailController($q,$http,$routeParams) {
       var self = this;

       self.setImage = function setImage(imageUrl) {
        self.mainImageUrl = imageUrl;
      };

       $q.all([

       $http.get('products/' + $routeParams.productId + '.json'),
       $http.get('http://localhost:5000/MainFunction/'+$routeParams.productId+'/'+$routeParams.productPrice)])
       .then(function(responses) {
         self.product = responses[0].data;
         self.setImage(self.product.images[0]);
         self.price = responses[1].data;
       });
      }
    ]
  });