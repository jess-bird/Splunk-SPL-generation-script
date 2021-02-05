# Splunk SPL generation script

## Automating generic Splunk query generation in python

The aim here is a reference set of tools to scale query generation for researchers and investigators on the fly.

The emphasis here is on inline queries, while not pretty or necessarily optimised to the n-th degree, these are rough and ready tools to achieve your goals as a researcher or investigator on the fly with new novel research topics.

This approach also minimises the impact of limitations on users in terms of permissions, publishing and collaboration in the Splunk space.

## Common error types encountered

### Lack of collaborative enablement

You find something cool, turn it into a widget/dashboard, click publish and set unrestricted viewing access only to have people turn around to you with empty dashboards.

This issue, assuming you can at least demonstrate the dashboards otherwise work on you own computer and login, is usually permissions on publishing based on roles and specific configurations of your Splunk instance --- inline searches negate this by running everything in the foreground.

### Time out errors

Want to get a data extract that's more than a few lines long, but keep getting time out errors? This is likely the load-balancing configuration time out setting in your Splunk instance. There is no inline solution to this as you will need to discuss either changing the loadbalancing time out limits at a sys admin level or perhaps go to the source data system directly and avoid Splunk all together.

