app.controller('add_user_controller', function($rootScope, $scope, $state, $http, $interval,fileUpload) {

    $scope.user = {};
    // calling our submit function.
    $scope.addUser = function() {

    $scope.uploadFile = function(){
        var file = $scope.myFile;
        var uploadUrl = "api/authentication_app/users/";
        fileUpload.uploadFileToUrl(file,$scope.user,uploadUrl);
    };
    $scope.uploadFile();

        // Posting data to php file
//        $http({
//                method: 'POST',
//                url: 'api/authentication_app/users/',
//                data: $scope.user, //forms user object
//                transformRequest: angular.identity,
//                headers: {'Content-Type': undefined}
//
//            })
//            .success(function(data) {
//                if (data.errors) {
//                    // Showing errors.
//                    $scope.errorName = data.errors.name;
//                    $scope.errorUserName = data.errors.username;
//                    $scope.errorEmail = data.errors.email;
//                    $scope.errorImage = data.errors.image;
//                } else {
//                    $scope.message = data.message;
//                    bootbox.alert("User added Succsfully");
//                }
//            });

    }

    $scope.getUser = function() {
    $http({
                method: 'GET',
                url: 'api/employe_details/' + $scope.id,
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
                }
            });
    }

});