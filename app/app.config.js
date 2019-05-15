'use strict';

angular.
  module('producatApp').
  config(['$routeProvider',
    function config($routeProvider) {
      $routeProvider.
        when('/homepage', {
          template: '<home-page></home-page>'
        }).
        when('/products', {
          template: '<product-list></product-list>'
        }).
        when('/products/:productId/:productPrice',{
          template: '<product-detail></product-detail>'
        }).
        otherwise('/homepage');
    }
  ]);