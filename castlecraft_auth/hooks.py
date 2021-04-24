# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "castlecraft_auth"
app_title = "Castlecraft Auth"
app_publisher = "Castlecraft"
app_description = "Castlecraft Authorization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@castlecraft.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/castlecraft_auth/css/castlecraft_auth.css"
# app_include_js = "/assets/castlecraft_auth/js/castlecraft_auth.js"

# include js, css files in header of web template
# web_include_css = "/assets/castlecraft_auth/css/castlecraft_auth.css"
# web_include_js = "/assets/castlecraft_auth/js/castlecraft_auth.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "castlecraft_auth/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "castlecraft_auth.utils.jinja_methods",
# 	"filters": "castlecraft_auth.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "castlecraft_auth.install.before_install"
# after_install = "castlecraft_auth.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "castlecraft_auth.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"castlecraft_auth.tasks.all"
# 	],
# 	"daily": [
# 		"castlecraft_auth.tasks.daily"
# 	],
# 	"hourly": [
# 		"castlecraft_auth.tasks.hourly"
# 	],
# 	"weekly": [
# 		"castlecraft_auth.tasks.weekly"
# 	]
# 	"monthly": [
# 		"castlecraft_auth.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "castlecraft_auth.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "castlecraft_auth.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "castlecraft_auth.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

auth_hooks = ["castlecraft_auth.auth.validate"]
