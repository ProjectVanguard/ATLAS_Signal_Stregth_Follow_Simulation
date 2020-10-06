# ATLAS_Signal_Stregth_Follow_Simulation

The program consists of the implementation of the algorithm that will be used in the ATLAS Signal Strength Follow system.
The algorithm was designed by the ATLAS DEV-OPS team and implemented by Manuel E. Portela

    Algorithm:

      1--Box Mission-the drone moves in a box and collects the points seen in Figure 1 below.

      2--It determines the strongest signal between the nine measurements.

      3--Case1: It creates a directional vector t0->tx, tx: being the strongest signal in the box.

        3.1--The drone will move in t0->tx direction as a scalar equal to the magnitude of t0->tx and collects signal strength measurements comparing them to the preview’s location measurement.

        3.2--Case1: The current signal is the strongest and the drone keeps moving.

        3.2--Case2: The current signal is weaker, and the drone moves to the preview’s location.

        3.3--The algorithm goes back to 1.

      3--Case2: t0 is the strongest signal and the algorithm stops and indicates that the animal is below inside a boxed raged relative to the box length chosen.



<img src="Box_Algorithm/box.jpg" width="600">
