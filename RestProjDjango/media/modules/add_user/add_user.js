app.controller('add_user_controller', function($rootScope, $scope, $state, $http, $interval) {

            //    $scope.addUser = function(){
            //            console.log($scope.user)}


            //$scope.Details = [];
            //$http.get('/api/Sessions/', '')
            //            .success(function (data) {
            //                $scope.Details = data;
            //            })


            $scope.user = {};
            // calling our submit function.
            $scope.addUser = function() {
                // Posting data to php file
                $http({
                        method: 'POST',
                        url: '/api/Sessions/',
                        data: $scope.user, //forms user object
//                        headers: {
//                            'Content-Type': 'application/x-www-form-urlencoded'
//                        }
                    })
                    .success(function(data) {
                        if (data.errors) {
                            // Showing errors.
                            $scope.errorName = data.errors.name;
                            $scope.errorUserName = data.errors.username;
                            $scope.errorEmail = data.errors.email;
                        } else {
                            $scope.message = data.message;
                        }
                    });

            }});