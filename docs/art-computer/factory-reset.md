# Factory Reset

Most people never need this page. The Art Computer looks after itself: it updates overnight, restarts cleanly, and recovers from most problems on its own. A factory reset is the last resort — for a device that no longer responds to the app, or one you are handing to someone else.

A factory reset erases everything on the device: Wi-Fi settings, the pairing with your account, and all downloaded artwork. The Art Computer returns to its factory software, then updates itself and walks you through [setup](./index.md) again. Your collection is safe — it lives with your account, not on the device — but artworks will re-download after setup.

---

## From the app (the normal way)

If the Art Computer still responds to the app, reset it from there: the app sends the reset command to the device (over the cloud, or directly on the local network). The screen shows a factory-reset notice, the device stops taking commands, and it restarts into its factory software. Use this path whenever it works — it needs no physical access beyond the screen. If the device comes back up still paired and playing your art, the reset did not take (the factory boot is a one-shot that falls back to the running system if it fails) — simply run it again.

## With the power cord (when nothing else works)

If the screen is stuck or black and the app cannot reach the device, there is a reset path that needs nothing but the power cord. It is deliberately awkward — five precise power cuts in a row — so it cannot happen by accident.

1. **Unplug** the Art Computer's power.
2. **Plug it back in** and watch the screen. When the **startup screen appears, unplug again.**
3. **Repeat** until you have cut the power **5 times**. Keep the rhythm going — a pause of more than about 2 minutes between cycles resets the count.
4. **Plug in once more and leave it.** The Art Computer restarts itself into a boot menu with **FF1 - Factory Reset** selected and a **60-second countdown** on screen.
5. Choose:
    - **Let the countdown finish** → the factory reset runs.
    - **Unplug during the countdown** → the reset is cancelled. Nothing is remembered; the next start is a completely normal one.

!!! warning "Once the reset starts, leave the power alone"
    Cancelling is only safe **during the countdown**. After it reaches zero the device is rewriting its system — keep it powered until the setup screen appears, usually within a few minutes.

### Rules the counter follows

- **Only power-cord cuts count.** Restarts from the app, overnight update restarts, and normal power-offs never add to the count — the sequence has to be you, at the device, unplugging it on purpose.
- **The timing must be deliberate.** Cut the power while the startup screen is showing, and keep each cycle under about 2 minutes. Slow or scattered power cuts — a storm, a flaky power strip — do not accumulate.
- **Nothing appears? Just wait.** If the countdown screen does not show up, the device simply boots normally. Unplug and try again, cutting power promptly each time the startup screen appears.

## With a keyboard (F2 into the boot menu)

If you have a USB keyboard handy, you can reach the same boot menu directly:

1. **Unplug** the power and connect a **USB keyboard** to the Art Computer.
2. **Plug the power back in** and immediately **tap F2 rapidly** on the keyboard, and keep tapping until the boot menu appears.
3. The window for this is brief and varies between units — it may take a few attempts. If the device boots normally instead, unplug and try again.
4. Use the **arrow keys** to select **FF1 - Factory Reset** and press **Enter**. The reset starts right away — there is no countdown on this path, since you confirm it yourself. Keep the device powered until the setup screen appears.

---

## After the reset

The Art Computer boots its factory software and shows the Wi-Fi setup screen (or, on Ethernet, goes straight to the pairing screen). From there it is a first-time [setup](./index.md): join Wi-Fi from your phone, let the device update itself to the current FF OS — it will not show the pairing screen until it has — then pair with the app and it returns to your art. Artworks re-download in the background; how long that takes depends on the size of your library and your connection.

!!! note "Very old factory software"
    A device that has sat on a shelf for a long time may carry factory software too old to update itself over the air. It will stop before the pairing screen. The fix is a [USB reinstall](./index.md#step-3-advanced-reinstall-ff-os-from-usb) of the current release image, after which setup proceeds normally.

!!! note "A reset device is an unclaimed device"
    After a factory reset, the Art Computer belongs to whoever pairs with it next. That is what makes it right for handing the device on — and worth knowing if the device is somewhere strangers can reach its power cord for several deliberate minutes.
