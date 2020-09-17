# imitation learning

Contains SAC imitation learning baseline expert trajs, results on mujoco.

This SAC code is modified upon https://github.com/rail-berkeley/softlearning, where we drop the ray-based training style to a easy-reading run on a single process. Expert performances are run using this code.

This data use a squash action (a is in [-1, 1])


|  Algs   | Envs  | Curve Data | Sampled Trajs | Plot Scripts |
|  ----  | ----  | ----  | ----  | ----  |
| SAC  | Ant, Hopper, Humanoid, HalfCheetah, Walker2d, Swimmer | N | Y | N

Expert Performances

SAC, 50 expert traj, Deterministic Policy in testing

| Envs | Mean | Std
| ----  | ----  | ----  |
| Ant | - | - |
| Hopper | 3402.9494 | 446.4877 |
| Humanoid | - | - |
| HalfCheetah | 13711.6445 | 111.4709 |
| Walker2d | 5259.4805 | 1329.5388 |
| Swimmer | - | - |
| AntSlim | 5418.8721 | 946.7947 |
| HumanoidSlim | 5346.6181 | 712.2214 |
| SwimmerSlim | 339.2811 | 0.7625 |

P.S.: *Slim envs are those envs that use a wrapper who remove some dimension of the observation.