
for thermostat_entity_id in hass.states.entity_ids("climate") :
	hass.services.call("group", "set", {
		"object_id": thermostat_entity_id.split(".")[1] + "_schedules",
		"name": "[" + hass.states.get(thermostat_entity_id).name + " Schedules]",
		"entities": [
			s.entity_id for s in hass.states.all("switch")
				if (s.entity_id.startswith("switch.schedule_")
					and len(s.entity_id) == 22
					and len([a for a in s.attributes["actions"] if a["service"] == "set_temperature" and a["entity"] == thermostat_entity_id]) > 0)
		]
	})
