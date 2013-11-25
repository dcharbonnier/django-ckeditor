{% load static %}
window.DJCKEDITOR = (typeof DJCKEDITOR == 'object') ? DJCKEDITOR : {};



DJCKEDITOR.configs = {{ merged_configs|safe }};

if (typeof CKEDITOR == 'object' && typeof CKEDITOR.config == 'object') {
    {% if debug %}
        CKEDITOR.timestamp = (new Date()).getTime();
    {% else %}
        CKEDITOR.timestamp = '{{ timestamp|escapejs }}';
    {% endif %}
    {% for plugin in plugins %}
        CKEDITOR.plugins.addExternal("{{plugin.0}}","{% static plugin.1%}/plugin.js");
    {% endfor %}
    CKEDITOR.config.jqueryOverrideVal = {{ jquery_override_val|safe }};

}

(function($) {

    if (typeof CKEDITOR == 'object' && CKEDITOR.jQuery === undefined) {
        CKEDITOR.jQuery = $;
    }

})((typeof grp == 'object' && grp.jQuery)
    ? grp.jQuery
    : (typeof django == 'object' && django.jQuery) ? django.jQuery : jQuery);