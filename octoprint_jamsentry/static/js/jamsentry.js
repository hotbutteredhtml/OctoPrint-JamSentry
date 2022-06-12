$(function() {
    class JamSentryViewModel {
        constructor(parameters) {
            var self = this;

            self.settingsViewModel = parameters[0];
        }
    }

        OCTOPRINT_VIEWMODELS.push([
            JamSentryViewModel,
            ["settingsViewModel"],
            ["#tab_plugin_jamsentry"]
        ]);
});