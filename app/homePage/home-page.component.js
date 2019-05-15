'use strict';

  angular.
  module('producatApp').
  component('homePage', {
    templateUrl: '/homePage/home-page.template.html',
    controller: ['$scope',
      function HomePageController($scope) {
        $scope.FirstName= "ProductList";
        $scope.Second= "ItemList"; 
      }]
    });
      
  
 


