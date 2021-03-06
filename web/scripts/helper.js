﻿var helper = {

    callService: function (url, data, verb, successFunction, options) {
        //makes an AJAX call to a service, handles success and failure

        var defaults = {
            showLoading: true, //boolean - show loading spinner
            loadingElementId: "loading", //string - the id of the loading spinner element
            logErrorToConsole: true, //boolean - log errors to the browser console
            showFriendlyErrorAlert: false, //boolean - show a friendly error alert
            showVerboseErrorAlert: true //boolean - show a verbose error alert
        }

        if (options) {
            defaults.showLoading = options.showLoading || defaults.showLoading;
            defaults.loadingElementId = options.loadingElementId || defaults.loadingElementId;
            defaults.logErrorToConsole = options.logErrorToConsole || defaults.logErrorToConsole;
            defaults.showFriendlyErrorAlert = options.showFriendlyErrorAlert || defaults.showFriendlyErrorAlert;
            defaults.showVerboseErrorAlert = options.showVerboseErrorAlert || defaults.showVerboseErrorAlert;
        }

        if (defaults.showLoading) {
            $("#" + defaults.loadingElementId).show();
        }

        if (verb == "GET") {
            if (data == {} || data == null) {
                data = "";
            }
        }
        else {
            if (data == "" || data == null) {
                data = {};
            }
            else {
                data = JSON.stringify(data);
            }
        }

        //make ajax call
        var promise = $.ajax({
            type: verb,
            url: url,
            data: data,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            crossDomain: true
        });

        //success
        promise.done(successFunction);

        //failure
        promise.fail(function (xhr, status, error) {

            if (defaults.logErrorToConsole) {
                console.log("xhr.status: " + xhr.status);
                console.log("xhr.readyState: " + xhr.readyState);
                console.log("xhr.responseText: " + xhr.responseText);
                console.log("xhr.responseXML: " + xhr.responseXML);
                console.log("status: " + status);
                console.log("error: " + error);
                console.log("url: " + url);
                console.log("data: " + data);
            }
            if (defaults.showFriendlyErrorAlert) {
                alert("An error occurred when attempting to call a service.")
            }
            if (defaults.showVerboseErrorAlert) {
                alert("An error occurred when attempting to call a service.\nThe error details are as follows.\nxhr.status: " + xhr.status + "\nxhr.readyState: " + xhr.readyState + "\nxhr.responseText: " + xhr.responseText + "\nxhr.responseXML: " + xhr.responseXML + "\nstatus: " + status + "\nerror: " + error + "\nurl: " + url + "\ndata: " + data);
            }
        });

        //always
        promise.always(function () {
            if (defaults.showLoading) {
                $("#" + defaults.loadingElementId).hide();
            }
        });

    },
    getQueryStringParams: function () {
        var params = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for (var i = 0; i < hashes.length; i++) {
            hash = hashes[i].split('=');
            params.push(hash[0]);
            params[hash[0]] = hash[1];
        }
        return params;
    }
};