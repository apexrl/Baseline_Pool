# imitation learning

Contains SAC imitation learning baseline expert trajs, results on mujoco.

This SAC code is modified upon https://github.com/rail-berkeley/softlearning, where we drop the ray-based training style to a easy-reading run on a single process. Expert performances are run using this code.

|  Algs   | Envs  | Curve Data | Sampled Trajs | Plot Scripts |
|  ----  | ----  | ----  | ----  | ----  |
| SAC  | Ant, Hopper, Humanoid, HalfCheetah, Walker2d, Swimmer | N | Y | N

Expert Performances

SAC, 50 expert traj

| Envs | Mean | Std
| ----  | ----  | ----  |
| Ant | 4162.8364 | 417.3424 |
| Hopper | 3219.4463 | 686.7828 |
| Humanoid | 2619.448 | 1107.4275 |
| HalfCheetah | 12796.926 | 139.16898 |
| Walker2d | 5259.4805 | 1329.5388 |
| Swimmer | 318.91995 | 2.0149245 |

