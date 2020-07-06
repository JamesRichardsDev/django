var initialize = function(navigator, user, token, urls) {
    navigator.id.watch({
        loggedInUser: user,
        onlogin: function(assertion) {
            $.post(urls.login, { assertion: assertion, csrfmiddlewaretoken: token })
                .done(function() { window.location.reload(); }).fail(function() { navigator.id.logout(); });
        },
        onlogout: function() {}
    })

    window.Superlists = {
        Accounts: {
            initialize: initialize
        }
    };
}