
hass.services.call("group", "set", {
	"object_id": "all_thermostat_schedules",
	"name": "[All Thermostat Schedules]",
	"entities": [
		switch_.entity_id for switch_ in hass.states.all("switch")
			if (switch_.entity_id.startswith("switch.schedule_")
				and len(switch_.entity_id) == 22
				and len([switch_action_ for switch_action_ in switch_.attributes["actions"]
					if switch_action_["service"] == "climate.set_temperature"]) > 0)
	]
})
