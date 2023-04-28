{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    just
    gnumake
    (pkgs.python310.withPackages (py: [
      py.psycopg2
      py.pip
      py.virtualenv
    ]))
  ];
}
