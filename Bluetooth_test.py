import bluetooth

def discover_devices():
    print("Searching for nearby devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, device_id=-1)
    print("Found {} devices:".format(len(nearby_devices)))
    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
    return nearby_devices

def connect_to_device(device_address):
    print("Connecting to device...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1  # RFCOMM port number
    try:
        sock.connect((device_address, port))
        print("Connected successfully to", device_address)
        return sock
    except Exception as e:
        print("Connection failed:", e)
        return None

def main():
    devices = discover_devices()
    if not devices:
        print("No devices found. Exiting.")
        return
    
    device_address = input("Enter the MAC address of the device you want to connect to: ")
    
    if device_address not in [addr for addr, _ in devices]:
        print("Device not found. Exiting.")
        return
    
    socket = connect_to_device(device_address)
    if socket:
        # You can now send/receive data through the socket
        # For example:
        # socket.send("Hello, Bluetooth Device!")
        # data = socket.recv(1024)
        # print("Received:", data)
        # Don't forget to close the socket when you're done:
        # socket.close()


main()
