
for thermostat_ in hass.states.all("climate") :
	hass.services.call("group", "set", {
		"object_id": thermostat_.object_id + "_schedules",
		"name": "[" + thermostat_.name + " Schedules]",
		"entities": [
			switch_.entity_id for switch_ in hass.states.all("switch")
				if (switch_.entity_id.startswith("switch.schedule_")
					and len([switch_action_ for switch_action_ in switch_.attributes.get("actions", [])
						if switch_action_["service"] == "climate.set_temperature"
							and switch_action_["entity_id"] == thermostat_.entity_id]) > 0)
		]
	})
