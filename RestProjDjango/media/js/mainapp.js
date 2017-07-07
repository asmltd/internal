var app = angular.module('internalApp',['ui.router'])


app.config(function ($stateProvider, $urlRouterProvider, $httpProvider) {


    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('dashboard_box', {
            url: '/',
            templateUrl:'/media/modules/dashboard/dashboard_box.html?v=' + window.version,
            controller: 'dashboard_box_controller'
        });

        });

