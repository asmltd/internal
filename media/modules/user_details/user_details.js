app.controller('user_details', function($rootScope, $scope, $state, $http, $interval,$window) {
    $scope.Details = [];

    $scope.loadUser = function() {
        $http.get('api/authentication_app/users/', '')
            .success(function(data) {
                $scope.Details = data;
            })
    }

    $scope.loadUser();

    $scope.del_user = function(id) {
        $http({
                method: 'DELETE',
                url: 'api/authentication_app/users/' + id + "/",
            })
            .success(function(data) {
                $scope.loadUser();
                bootbox.alert("Deleted");
            });
    }


     $scope.edit_user = function(id){

     $state.go('update_user',{id:id});

     console.log(id);

    }
});