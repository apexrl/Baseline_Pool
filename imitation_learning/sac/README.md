# imitation learning

Contains SAC imitation learning baseline expert trajs, results on mujoco.

This SAC code is modified upon https://github.com/rail-berkeley/softlearning, where we drop the ray-based training style to a easy-reading run on a single process. Expert performances are run using this code.

This data use a squash action (a is in [-1, 1]), it is ok since the action space in mujoco is also in [-1, 1]


|  Algs   | Envs  | Curve Data | Sampled Trajs | Plot Scripts |
|  ----  | ----  | ----  | ----  | ----  |
| SAC  | Pendulum, InvertedPendulum, InvertedDoublePendulum, Ant, Hopper, Humanoid, HalfCheetah, Walker2d, Swimmer | N | Y | N

Expert Performances

SAC, 50 expert traj, Deterministic Policy in testing

| Envs | Mean | Std
| ----  | ----  | ----  |
| Pendulum | 139.7313 | 79.8126 |
| InvertedPendulum | 1000.0000 | 0.0000 |
| InvertedDoublePendulum | 9358.8740 | 0.1043
| Ant | 5404.5532 | 1520.4961 |
| Hopper | 3402.9494 | 446.4877 |
| Humanoid | 6043.9907 | 726.1788 |
| HalfCheetah | 13711.6445 | 111.4709 |
| Walker2d | 5639.3267 | 29.9715 |
| Swimmer | 139.2806 | 1.1204 |
| AntSlim | 5418.8721 | 946.7947 |
| HumanoidSlim | 5346.6181 | 712.2214 |
| SwimmerSlim | 339.2811 | 0.7625 |

Random Performance

| Envs | Mean | Std
| ----  | ----  | ----  |
| Pendulum | -1494.1357 | 265.8315 |
| InvertedPendulum | 25.2800 | 5.5318 |
| InvertedDoublePendulum | 78.2829 | 10.7335
| Ant | 713.5986 | 203.9204 |
| Hopper | 13.0901 | 0.1022 |
| Humanoid | 64.7384 | 2.3037 |
| HalfCheetah | 74.4849 | 12.3917 |
| Walker2d | 7.0708 | 0.1292 |
| Swimmer | 15.5430 | 6.6655 |

P.S.: *Slim envs are those envs that use a wrapper who remove some dimension of the observation.
