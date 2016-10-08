#!/bin/bash

#
# Copy of config.sh from official library + custom tests
# Can't seem to get two config files working
# Will need to update this periodically

set -e

globalTests+=(
	gmt
)

testAlias+=(

)

imageTests+=(
	[$APP_TEST_IMAGE]='
	'
)

globalExcludeTests+=(
	# single-binary images
	[${APP_TEST_IMAGE}_utc]=1
	[${APP_TEST_IMAGE}_gmt]=1
	[${APP_TEST_IMAGE}_override-cmd]=1
)
