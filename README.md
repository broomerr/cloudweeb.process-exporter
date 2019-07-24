Cloudweeb Process-exporter
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.process-exporter.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.process-exporter)

Ansible role to install process-exporter

Requirements
------------

None

Role Variables
--------------

```YAML
# process_exporter version to be installed
process_exporter_version: 0.5.0

# process_exporter config file path
process_exporter_config_file: /etc/process_exporter.yml

# process_exporter listen address
process_exporter_web_listen_address: 0.0.0.0:9256

# This is list of process names that want to be monitor
# comm is the second field of /proc/<pid>/stat minus parens.
# It is the base executable name, truncated at 15 chars.
# It cannot be modified by the program, unlike exe.
# - comm:
#   - bash

# exe is argv[0]. If no slashes, only basename of argv[0] need match.
# If exe contains slashes, argv[0] must match exactly.
# - exe:
#   - postgres
#   - /usr/local/bin/prometheus

# cmdline is a list of regexps applied to argv.
# Each must match, and any captures are added to the .Matches map.
# - name: "{{.ExeFull}}:{{.Matches.Cfgfile}}"
#   exe:
#   - /usr/local/bin/process-exporter
#   cmdline:
#   - -config.path\s+(?P<Cfgfile>\S+)
process_exporter_process_names: []
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        process_exporter_process_names:
          - comm:
            - bash
          - name: "{% raw %}{{.ExeFull}}:{{.Matches.Cfgfile}}{% endraw %}"
            exe: 
            - /usr/bin/process-exporter
            cmdline: 
            - -config.path\\s+(?P<Cfgfile>\\S+)
      roles:
         - role: cloudweeb.process-exporter

License
-------

MIT

Author Information
------------------

Agnesius Santo Naibaho
