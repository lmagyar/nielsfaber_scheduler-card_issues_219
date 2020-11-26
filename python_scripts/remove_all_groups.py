
for s in hass.states.all("group") :
	if s.name.startswith("[") and s.name.endswith("]") :
		hass.services.call("group", "remove", {
			"object_id": s.object_id
		})
