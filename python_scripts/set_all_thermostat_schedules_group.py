
hass.services.call("group", "set", {
	"object_id": "all_thermostat_schedules",
	"name": "[All Thermostat Schedules]",
	"entities": [
		s.entity_id for s in hass.states.all("switch")
			if (s.entity_id.startswith("switch.schedule_")
				and len(s.entity_id) == 22
				and len([a for a in s.attributes["actions"] if a["service"] == "set_temperature"]) > 0)
	]
})
