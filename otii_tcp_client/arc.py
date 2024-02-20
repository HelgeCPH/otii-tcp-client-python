#!/usr/bin/env python
#coding: utf-8
from enum import Enum
from otii_tcp_client import otii_connection, otii_exception
from otii_tcp_client.toggle import Toggle


class Arc:
    """ Class to define an Arc device.
        Includes operations that can be run on the Arc.

    Attributes:
        type (str): Device type, "Arc" for Arc devices.
        id (str): ID of the Arc device.
        name (str): Name of the Arc device.
        connection (:obj:OtiiConnection): Object to handle connection to the Otii server.

    """
    def __init__(self, device_dict, connection):
        """
        Args:
            device_dict (dict): Dictionary with Arc parameters.
            connection (:obj:OtiiConnection): Object to handle connection to the Otii server.

        """
        self.type = device_dict["type"]
        self.id = device_dict["device_id"]
        self.name = device_dict["name"]
        self.connection = connection

    def calibrate(self):
        """ Perform internal calibration of an Arc device.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_calibrate", "data": data}
        response = self.connection.send_and_receive(request, 10)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def toggle_5v(self, toggle):
        """ Enable or disable 5V pin.

        Args:
            toggle (:obj:Toggle): Toggle.ON to enable 5V, Toggle.OFF to disable.

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_enable_5v", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_5v(self):
        """ Enable 5V pin.
        """
        self.toggle_5v(Toggle.ON)

    def disable_5v(self):
        """ Disable 5V pin.
        """
        self.toggle_5v(Toggle.OFF)

    def toggle_battery_profiling(self, toggle):
        """ This starts or stops the discharge profiling of a connected battery.

        Args:
            toggle (:obj:Toggle): Toggle.ON to start battery profiling, Toggle.OFF to stop.
        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_enable_battery_profiling", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_battery_profiling(self):
        """ This starts the discharge profiling of a connected battery.
        """
        self.toggle_battery_profiling(Toggle.ON)

    def disable_battery_profiling(self):
        """ This will stop the discharge profiling of a connected battery.
        """
        self.toggle_battery_profiling(Toggle.OFF)

    def toggle_channel(self, channel, toggle):
        """ Enable or disable measurement channel.

        Args:
            channel (:obj:Channel): Name of the channel to enable or disable.
            toggle (:obj:Toggle): True to enable channel, False to disable.

        """
        data = {"device_id": self.id, "channel": channel.value, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_enable_channel", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_channel(self, channel):
        """ Enable a measurement channel.

        Args:
            channel (:obj:Channel): Name of the channel to enable.
        """
        self.toggle_channel(channel, Toggle.ON)

    def disable_channel(self, channel):
        """ Enable a measurement channel.

        Args:
            channel (:obj:Channel): Name of the channel to disable.
        """
        self.toggle_channel(channel, Toggle.OFF)

    def toggle_exp_port(self, toggle):
        """ Enable or disable expansion port.

        Args:
            toggle (:obj:Toggle): Toggle.ON to enable expansion port, Toggle.OFF to disable.

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_enable_exp_port", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_exp_port(self):
        """ Enable expansion port.
        """
        self.toggle_exp_port(Toggle.ON)

    def disable_exp_port(self):
        """ Disable expansion port.
        """
        self.toggle_exp_port(Toggle.OFF)

    def toggle_uart(self, toggle):
        """ Enable or disable UART.

        Args:
            toggle (:obj:Toggle): Toggle.ON to enable UART, Toggle.OFF to disable.
        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_enable_uart", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_uart(self):
        """ Enable UART.
        """
        self.toggle_uart(Toggle.ON)

    def disable_uart(self):
        """ Disable UART.
        """
        self.toggle_uart(Toggle.OFF)

    def get_4wire(self):
        """ Get the 4-wire measurement state.

        Returns:
            str: The current state, "cal_invalid", "disabled", "inactive" or "active".

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_4wire", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_adc_resistor(self):
        """ Get adc resistor value.

        Returns:
            float: ADC resistor value (Ohm).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_adc_resistor", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_channel_samplerate(self, channel):
        """ Get channel sample rate.

        Args:
            channel (:obj:Channel): Name of the channel to get the sample rate for.

        Returns:
            int: Sample rate for channel

        """
        data = {"device_id": self.id, "channel": channel.value}
        request = {"type": "request", "cmd": "arc_get_channel_samplerate", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_exp_voltage(self):
        """ Get the voltage of the expansion port.

        Returns:
            float: Voltage value on the expansion port (V).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_exp_voltage", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_gpi(self, pin):
        """ Get the state of one of the GPI pins.

        Args:
            pin (int): ID of the GPI pin to get state of, 1 or 2.

        Returns:
            bool: State of the GPI pin.

        """
        data = {"device_id": self.id, "pin": pin}
        request = {"type": "request", "cmd": "arc_get_gpi", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_main(self):
        """ Get the state of the main power.

        Returns:
            bool: State of the main power.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_main", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_main_voltage(self):
        """ Get main voltage value.

        Returns:
            float: Main voltage value (V).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_main_voltage", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_max_current(self):
        """ Get the max allowed current.

        Returns:
            float: Value max current is set to (A).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_max_current", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_range(self):
        """ Get the current measurement range on the main output.

        Returns:
            str: Current measurement range mode on main, "low" or "high".

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_range", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["range"]

    def get_rx(self):
        """ The RX pin can be used as a GPI when the UART is disabled.

        Returns:
            bool: State of the RX pin.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_rx", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_src_cur_limit_enabled(self):
        """ Get current state of voltage source current limiting.

        Returns:
            bool: True if set to constant current, false if set to cut-off.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_src_cur_limit_enabled", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["enabled"]

    def get_supplies(self):
        """ Get a list of all available supplies. Supply ID 0 always refers to the power box.

        Returns:
            list: List of supply objects.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supplies", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["supplies"]

    def get_supply(self):
        """ Get current power supply ID.

        Returns:
            int: ID of current supply.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supply", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["supply_id"]

    def get_supply_parallel(self):
        """ Get current number of simulated batteries in parallel.

        Returns:
            int: Number of batteries in parallel.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supply_parallel", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_supply_series(self):
        """ Get current number of simulated batteries in series.

        Returns:
            int: Number of batteries in series.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supply_series", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_supply_soc_tracking(self):
        """ Get current state of power supply State of Charge tracking.

        Returns:
            bool: True if State fo Charge tracking is enabled, False if disabled.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supply_soc_tracking", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["enabled"]

    def get_supply_used_capacity(self):
        """ Get current power supply used capacity.

        Returns:
            float: Used capacity in coulomb (C).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_supply_used_capacity", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_uart_baudrate(self):
        """ Get the UART baud rate.

        Returns:
            int: Value UART baud rate is set to.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_uart_baudrate", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_value(self, channel):
        """ Get value from specified channel.
        This is not available for the UART_LOGS (rx) channel.

        Args:
            channel (:obj:Channel): Name of the channel to get value from.

        Returns:
            float: Present value in the channel (A/V/°C/Digital).

        """
        data = {"device_id": self.id, "channel": channel.value}
        request = {"type": "request", "cmd": "arc_get_value", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def get_version(self):
        """ Get hardware and firmware versions of device.

        Returns:
            dict: Dictionary including keys hw_version (str) and fw_version (str).

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_get_version", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]

    def is_connected(self):
        """ Check if a device is connected.

        Returns:
            bool: True if device is connected, False otherwise.

        """
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_is_connected", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["connected"]

    def toggle_4wire(self, toggle):
        """ Enable or disable 4-wire measurements using Sense+/-.

        Args:
            toggle (:obj:Toggle): Toggle.ON to enable 4-wire, Toggle.OFF to disable

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_set_4wire", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_4wire(self):
        """ Enable 4-wire measurements using Sense+/-.
        """
        self.toggle_4wire(Toggle.ON)

    def disable_4wire(self):
        """ Disable 4-wire measurements using Sense+/-.
        """
        self.toggle_4wire(Toggle.OFF)

    def set_adc_resistor(self, value):
        """ Set the value of the shunt resistor for the ADC.

        Args:
            value (float): Value to set ADC resistor to, value should be between 0.001-22 (Ohm).

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_adc_resistor", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_battery_profile(self, value):
        """ Set the battery profile.

        Args:
            value (list): The list of battery profile step dicts (max 10). Each dict is of the { "current|resistance|power" : SI value, "duration" : seconds } form.

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_battery_profile", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_channel_samplerate(self, channel, value):
        """ Set the sample rate of a channel

        Args:
            channel (:obj:Channel): Name of the channel to set the sample rate for.
            value (int): The sample rate to set

        """
        data = {"device_id": self.id, "channel": channel, "value": value.value}
        request = {"type": "request", "cmd": "arc_set_channel_samplerate", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_exp_voltage(self, value):
        """ Set the voltage of the expansion port.

        Args:
            value (float): Value to set expansion port voltage to, value should be between 1.2-5 (V).

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_exp_voltage", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def toggle_gpo(self, pin, toggle):
        """ Set the state of one of the GPO pins.

        Args:
            pin (int): ID of the GPO pin to set state of, 1 or 2.
            toggle (:obj:Toggle): Toggle.ON to enable GPO output, Toggle.OFF to disable.

        """
        data = {"device_id": self.id, "pin": pin, "value": toggle.value}
        request = {"type": "request", "cmd": "arc_set_gpo", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_gpo(self, pin):
        """ Enable one of the GPO pins.

        Args:
            pin (int): ID of the GPO pin to enable, 1 or 2.
        """
        self.toggle_gpo(pin, Toggle.ON)

    def disable_gpo(self, pin):
        """ Disable one of the GPO pins.

        Args:
            pin (int): ID of the GPO pin to disnable, 1 or 2.
        """
        self.toggle_gpo(pin, Toggle.OFF)

    def toggle_main(self, toggle):
        """ Turn on or off main power on a device.

        Args:
            toggle (:obj:Toggle): Toggle.ON to turn on main power, Toggle.OFF to turn off.

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_set_main", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_main(self):
        """ Turn on main power on a device.
        """
        self.toggle_main(Toggle.ON)

    def disable_main(self):
        """ Turn off main power on a device.
        """
        self.toggle_main(Toggle.OFF)

    def set_main_current(self, value):
        """ Set the main current on Arc. Used when the Otii device is set in constant current mode.

        Args:
            value (float): Current to set in (A).

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_main_current", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_main_voltage(self, value):
        """ Get data entries from a specified channel of a specific recording.

        Args:
            value (float): Value to set main voltage to (V).

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_main_voltage", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_max_current(self, value):
        """ When the current exceeds this value, the main power will cut off.

        Args:
            value (float): Value to set max current to, value should be between 0.001-5 (A).

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_max_current", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_power_regulation(self, mode):
        """ Set power regulation mode.

        Args:
            mode (float): One of the following: "voltage", "current", "off".

        """
        data = {"device_id": self.id, "mode": mode}
        request = {"type": "request", "cmd": "arc_set_power_regulation", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def set_range(self, range):
        """ Set the main outputs measurement range.

        Args:
            range (str): Current measurement range mode to set on main. "low" enables auto-range, "high" force high-range.

        """
        data = {"device_id": self.id, "range": range}
        request = {"type": "request", "cmd": "arc_set_range", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def toggle_src_cur_limit(self, toggle):
        """ Enable voltage source current limit (CC) operation.

        Args:
            toggle (:obj:Toggle): Toggle.ON means enable constant current, Toggle.OFF means cut-off.

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_set_src_cur_limit_enabled", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_toggle_src_cur_limit(self):
        """ Enable voltage source current limit (CC) operation.
        """
        self.toggle_src_cur_limit(Toggle.ON)

    def disable_toggle_src_cur_limit(self):
        """ Disable voltage source current limit (CC) operation.
        """
        self.toggle_src_cur_limit(Toggle.OFF)

    def set_supply(self, supply_id, series = 1, parallel = 1):
        """ Set power supply type.

        Args:
            supply_id (int): ID of supply type, as returned by get_supplies.
            series (int, optional): Number of batteries in series, defaults to 1.
            parallel (int, optional): Number of batteries in parallel, defaults to 1.

        """
        data = {"device_id": self.id, "supply_id": supply_id, "series": series, "parallel": parallel}
        request = {"type": "request", "cmd": "arc_set_supply", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def toggle_supply_soc_tracking(self, toggle):
        """ Set power supply State of Charge tracking.

        Args:
            toggle (:obj:Toggle): Toggle.ON to enable State of Charge tracking, Toggle.OFF to disable.

        """
        data = {"device_id": self.id, "enable": toggle.value}
        request = {"type": "request", "cmd": "arc_set_supply_soc_tracking", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_supply_soc_tracking(self):
        """ Enable power supply State of Charge tracking.
        """
        self.toggle_supply_soc_tracking(Toggle.ON)

    def disable_supply_soc_tracking(self):
        """ Disable power supply State of Charge tracking.
        """
        self.toggle_supply_soc_tracking(Toggle.OFF)

    def set_supply_used_capacity(self, value):
        """ Set power supply used capacity.

        Args:
            value (float): Capacity used in coulombs (C), multiply mAh by 3.6 to get C.

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_supply_used_capacity", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def toggle_tx(self, toggle):
        """ The TX pin can be used as a GPO when the UART is disabled.

        Args:
            toggle (:objToggle:): Toggle.ON to enable TX output, Toggle.OFF to disable.

        """
        data = {"device_id": self.id, "value": toggle.value}
        request = {"type": "request", "cmd": "arc_set_tx", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def enable_tx(self):
        """ The TX pin can be used as a GPO when the UART is disabled.
        """
        self.toggle_tx(Toggle.ON)

    def disable_tx(self):
        """ The TX pin can be used as a GPO when the UART is disabled.
        """
        self.toggle_tx(Toggle.OFF)

    def set_uart_baudrate(self, value):
        """ Set UART baud rate.

        Args:
            value (int): Value to set UART baud rate to.

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_set_uart_baudrate", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def wait_for_battery_data(self, timeout):
        """ Wait for battery data.

        Args:
            timeout (int): Maximum timeout in ms. May time out earlier if another Arc is returning battery data.
        Returns:
            dict: Battery data dict or None if timeout. The dict will contain "timestamp" in seconds,
                           "iteration", "step", "voltage" at the end of the current step and "discharge" in coulombs accumulating
                           the total discharge of the battery since profiling start.

        """
        data = {"device_id": self.id, "timeout": timeout}
        request = {"type": "request", "cmd": "arc_wait_for_battery_data", "data": data}
        response = self.connection.send_and_receive(request, 60 + (timeout / 1000))
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"]["value"]

    def write_tx(self, value):
        """ Write data to TX.

        Args:
            value (str): Data to write to TX.

        """
        data = {"device_id": self.id, "value": value}
        request = {"type": "request", "cmd": "arc_write_tx", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def get_property(self, name):
        data = {"device_id": self.id, "name": name}
        request = {"type": "request", "cmd": "arc_get_property", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)
        return response["data"].get("value", None)

    def set_property(self, name, value):
        data = {"device_id": self.id, "name": name, "value": value}
        request = {"type": "request", "cmd": "arc_set_property", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def commit(self):
        data = {"device_id": self.id}
        request = {"type": "request", "cmd": "arc_commit", "data": data}
        response = self.connection.send_and_receive(request)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)

    def firmware_upgrade(self, filename = None):
        """ Initiate device firmware update.

        Args:
            filename (str, optional): Firmware filename.

        """
        data = {"device_id": self.id, "filename": filename}
        request = {"type": "request", "cmd": "arc_firmware_upgrade", "data": data}
        response = self.connection.send_and_receive(request, 15)
        if response["type"] == "error":
            raise otii_exception.Otii_Exception(response)


class Channel(Enum):
    """ All channels of an ARC device and their mapping to strings that are
    understood by the TCP server.

    Use these values as input to the `Arc.enable_channel` method or for the
    `get_*` methods of the ``Recording` class.
    """
    # Identifier   String value   Unit
    MAIN_CURRENT = "mc"         # A
    MAIN_VOLTAGE = "mv"         # V
    MAIN_ENERGY = "me"          # J
    ADC_CURRENT = "ac"          # A
    ADC_VOLTAGE = "av"          # V
    ADC_ENERGY = "ae"           # J
    SENSE_MINUS_VOLTAGE = "sn"  # V
    SENSE_PLUS_VOLTAGE = "sp"   # V
    VBUS = "vb"                 # V
    TEMPERATURE = "tp"          # °C
    UART_LOGS = "rx"            # text
    GPI_1 = "i1"
    GPI_2 = "i2"
