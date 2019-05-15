'use strict';

// Register `productList` component, along with its associated controller and template
angular.
  module('productList').
  component('productList', {
    templateUrl: 'productList/product-list.template.html',
    controller: ['$http', function PhoneListController($http) {
      var self = this;
      self.orderProp = 'age';

      $http.get('products/products.json').then(function(response) {
        self.products = response.data;
      });
    }]
  });