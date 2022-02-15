# Python client for Otii TCP-server

The otii_tcp_client is a Python package for controlling the [Otii Automation Toolbox](https://www.qoitech.com/automation-toolbox/).

New functionality in client v1.0.4 requiring [Otii software v2.8.4 or later](https://www.qoitech.com/download):
- New optinal `timeout` parameter added to `otii.get_devices`, that specifies the time in seconds to wait for an avaliable device
- Improved handling of TCP requests
- Added `arc.get_main` command

New functionality in client v1.0.3 requiring [Otii software v2.7.2 or later](https://www.qoitech.com/download):
- `Recording` object now exposes the start time as `start_time`

New functionality in client v1.0.2 requiring [Otii software v2.7.1 or later](https://www.qoitech.com/download):
- `arc.[gs]et_src_cur_limit_enabled` commands
- `arc.[gs]et_4wire` commands
- `arc.enable_battery_profiling`, `arc.set_battery_profile` and `arc.wait_for_battery_data` commands
