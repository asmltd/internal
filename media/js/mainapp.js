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

        $stateProvider
        .state('add_user', {
            url: '/add_user',
            templateUrl: '/media/modules/add_user/add_user.html?v=' + window.version,
            controller: 'add_user_controller'
        });

        $stateProvider
        .state('update_user', {
            url: '/update_user/:id',
            templateUrl: '/media/modules/update_user/update_user.html?v=' + window.version,
            controller: 'update_user_controller'
        });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        });

