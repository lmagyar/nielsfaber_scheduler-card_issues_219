
hass.services.call("group", "set", {
	"object_id": "all_thermostats",
	"name": "[All Thermostats]",
	"entities": hass.states.entity_ids("climate")
})
