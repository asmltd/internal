app.controller('update_user_controller', function($rootScope, $scope, $state, $http, $interval,$stateParams) {

    $scope.user = {};
    $scope.id = $stateParams.id;
    // calling our submit function.
    $scope.UpdateUser = function() {
        // Posting data to php file
        $http({
                method: 'PATCH',
                url: 'api/authentication_app/users/' + $scope.id + "/",
                data: $scope.user, //forms user object
            })
            .success(function(data) {
                if (data.errors) {
                    // Showing errors.
                    $scope.errorName = data.errors.name;
                    $scope.errorUserName = data.errors.username;
                    $scope.errorEmail = data.errors.email;
                } else {
                    $scope.message = data.message;
                    bootbox.alert("User Updated Succsfully");
                }
            });
    }
    $scope.getUser = function(id) {
        $http.get('api/authentication_app/users/' + $scope.id + "/", '')
            .success(function(data) {
                $scope.user = data;
//               console.log($scope.Details)
            })
    }

    $scope.getUser();



});