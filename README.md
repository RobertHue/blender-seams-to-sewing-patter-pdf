# Blender Seams to Sewing Pattern

An add-on for Blender that assists with setting up 2D sewing patterns from 3D models, for cloth simulation and real-life sewing.

![](https://blenderartists.org/uploads/default/optimized/4X/3/7/9/379d4a76a9022a7ff338773500784e22500dd8f6_2_690x207.jpeg)\
[![](https://img.youtube.com/vi/EZr__pTxsKk/mqdefault.jpg)\
▶ Quick guide on youtube](https://www.youtube.com/watch?v=EZr__pTxsKk)

## Table of Contents

- [Blender Seams to Sewing Pattern](#blender-seams-to-sewing-pattern)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Very Brief Overview](#very-brief-overview)
  - [Development](#development)
  - [Repository structure](#repository-structure)
    - [Installation prerequisites](#installation-prerequisites)
    - [Possible Issues](#possible-issues)
  - [Reporting Issues](#reporting-issues)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)
  - [Sustainability and Ethics 🌱](#sustainability-and-ethics-)
  - [Known Issues](#known-issues)

## Installation

Download the archive here:\
https://gitlab.com/thomaskole/blender-seams-to-sewing-pattern/-/archive/master/blender-seams-to-sewing-pattern-master.zip

In Blender, go to `Edit > ⚙️ Preferences > Install..` and select the zip file you just downloaded.\
Enable the add-on in the list.

## Usage

For a overview of how to use the Addon refer to https://www.thomaskole.nl/s2s/

Note that `UV Editor > Overlays > UV Editing > Display Stretch > Type: Area` is not part of this Addon and a Blender specific feature but useful for this Addon.
If there are places that show up too green, it will apply too much tension to the fabric.

### Very Brief Overview

![triceratops showcase](https://gitlab.com/thomaskole/blender-seams-to-sewing-pattern/-/wikis/uploads/2364f88e60b43cf0cc44309c2e4f15be/triceratops.gif)

`Object > Seams to Sewing Pattern > Seams to Sewing Pattern`\
turns your mesh into a sewing patten based on it's UV layout.

`Object > Seams to Sewing Pattern > Quick Clothsim`\
Applies some basic cloth sim options to your Object

`Object > Seams to Sewing Pattern > Export Sewing Pattern (.svg)`\
Exports your sewing pattern to a .SVG file for printing and sewing in real life.

`Edge > Clean up Knife Cut`\
Clean up selected edges after you used the knife tool on a mesh

## Development

## Repository structure

The repository is structured as follows:

- `.vscode/`: workspace configuration for [VSCode]
- `pyproject.toml`: configuration file for [Poetry], [isort], [Black], [mypy], [Ruff] and [pyright]
- `README.md`: the README file that you are reading right now

### Installation prerequisites

- [Git]
- [VSCode]
- [Python] (see `pyproject.toml` for it's version)
- Install [Poetry], as follows:

   ```console
   python -m pip install --upgrade pip
   python -m pip install --user pipx
   python -m pipx ensurepath
   pipx install poetry
   ```

To install these dependencies, just execute the following command:

   ```console
   poetry install
   ```

### Possible Issues

If you get the following error while launcher `Blender: Start`

`could not install debugpy blender addon`

Then manually install the requirements with the following command; replacing the x with your Blender version:
`c:\Program Files\Blender Foundation\Blender x\x\python\bin\python.EXE" -m pip install debugpy click flask`

As described in https://github.com/JacquesLucke/blender_vscode/issues/99#issuecomment-1065896620

## Reporting Issues

Something wrong? Please let me know.

There's a Blender Artists thread here: https://blenderartists.org/t/1248713 \
You can also add an issue here on GitLab,\
or get in touch with me otherwise: \
http://www.thomaskole.nl

## Troubleshooting

**I'm getting a python error**\
That's bad, please let me know the error and how you triggered it.

**After unfolding, there's some weird long triangles /strips flying out**\
Most likely some non-manifold geometry, overlapping vertices, or bad normals.\
Disable the remesh option and see where it goes wrong in your mesh / UV'seams

**My mesh is imploding on itself during clothsim**\
Yeah, clothsim... Try balancing the "pressure" and "sewing force".\
It can help to keyframe the "pressure" to something very high on frame 1 and decrease over time.

## License

GPL V2:\
[GPL-license.txt](./GPL-license.txt)

## Sustainability and Ethics 🌱

The production of natural textiles often involve overuse of water, fertilizers and perticides.\
Synthetic textiles are a large, often overlooked source of plastic pollution.\
The textile industry is often associated with unethical work conditions.

If you wish to use this add-on for real-life sewing purposes, I ask of you to use only sustainable / second-hand fabrics, and fair labour.

See also:\
[Sustainability-and-Ethics-notice.txt](./Sustainability-and-Ethics-notice.txt)

## Known Issues

- UV's are messed up after Remesh

[Git]: https://git-scm.com/downloads
[Python]: https://www.python.org/
[VSCode]: https://code.visualstudio.com/
[Poetry]: https://python-poetry.org/
[isort]: https://pycqa.github.io/isort/
[Black]: https://github.com/psf/black
[mypy]: https://mypy.readthedocs.io/en/stable/
[Ruff]: https://github.com/astral-sh/ruff
[pyright]: https://github.com/microsoft/pyright
