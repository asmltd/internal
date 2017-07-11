var app = angular.module('internalApp',['ui.router'])


app.config(function ($stateProvider, $urlRouterProvider, $httpProvider) {


    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('dashboard_box', {
            url: '/',
            templateUrl:'/media/modules/dashboard/dashboard_box.html?v=' + window.version,
            controller: 'dashboard_box'
        });

        $stateProvider
        .state('user_details', {
            url: '/user_details',
            templateUrl: '/media/modules/user_details/user_details.html?v=' + window.version,
            controller: 'user_details'
        });

        });

