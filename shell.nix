{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    ffmpeg
    (python3.withPackages (p: [
      p.discordpy
      p.pynacl
    ]))
  ];
}
