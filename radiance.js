

var app = angular.module("UserManagement", ['ngSanitize']);


//Controller Part
app.controller("UserManagementController", function($scope, $http) {

    //Initialize page with default data which is blank in this example
    $scope.tasks = [];

    $scope.selectedTask = null;
    $scope.createMode = false;

    //Now load the data from server
    _refreshPageData();

    $scope.extendTask = function (task) {
        $scope.selectedTask = task.ref;
        $scope.createMode = false;
        console.log(`selected task is $task.ref`);
        // _loadExtendedPanel(task.ref);
    }

    $scope.onFocus = function (value) {
        if (value) {
            $scope.createMode = value;
            $scope.selectedTask = null;
        }
    }

    $scope.htmlize = function(content) {
        return content.replace(new RegExp("\n", "g"), "<br/>");
    }

    function _refreshPageData() {

        for(var i in localStorage)
        {
            if (i.startsWith("titem.")) {
                // console.log(`Adding item to --scope-- key: ${i} value: ${localStorage[i]}`)
                var taskData = JSON.parse(localStorage[i]);
                $scope.tasks.push(taskData);
            }
        }

        console.log(`tasks have total items: ${$scope.tasks.length}`)
    }

    function _success(response) {
        _refreshPageData();
    }

    function _loadExtendedPanel(ref) {
        $http({
            method : 'GET',
            url : '/api/task/' + ref
        }).then(function successCallback(response) {

            $scope.selectedTaskDetails = response.data;

        }, function errorCallback(response) {

            console.log(response.statusText);
        });
    }

    function _error(response) {
        console.log(response.statusText);
    }

    //Clear the form
    function _clearForm() {
        $scope.form.firstName = "";
        $scope.form.lastName = "";
        $scope.form.email = "";
        $scope.form.id = -1;
    };
});


function dp() {
    for(var i in localStorage)
    {
        console.log(i);
        console.log(localStorage[i]);
        console.log(`key: ${i} value: ${localStorage[i]}`);
        // localList.push(localStorage[i]);
        // if (i.startsWith("titem.")) {
        //     localList.append(localStorage[i]);
        // }
    }
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function addSamples() {

    for (var i = 0; i<10; i++) {
        var ref = uuidv4();
        var task = {
            "ref": ref,
            "title": "Default title",
            "content": "Default content \n Hello content",
            "created_at": "2018-11-04",
            "due_date": "2018-11-15",
            "status": "active"
        }

        var storageKey = "titem." + ref;
        localStorage.setItem(storageKey, JSON.stringify(task));
    }
}

function cleardb() {

    var localList = [];

    for(var i in localStorage)
    {
        // console.log(localStorage[i]);
        localList.push(i);
        console.log(`Pushing the item: ${i}`)
        // if (i.startsWith("titem.")) {
        //     localList.append(localStorage[i]);
        // }
    }

    for (var k in localList) {
        console.log(`removing ${k}, ${localList[k]}`);
        localStorage.removeItem(localList[k]);
    }
}
