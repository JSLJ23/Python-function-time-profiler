# shell.nix
{ pkgs ? import <nixpkgs> {
    config = {
        allowUnfree = true;
        cudaSupport = true;
    };
} }:

with pkgs;

let
    my-python = pkgs.python39;
        python-with-my-packages = my-python.withPackages (p: with p; [
        pandas
        ViennaRNA # ViennaRNA is used here as a demo function for a slow function.
        # other python packages you want.
    ]);

in
pkgs.mkShell {
    buildInputs = [
        python-with-my-packages
        # other dependencies
    ];

    shellHook = ''
        which python
        echo "You are running in a Nix environment!"
        du -hc --max-depth=0 /nix/store # Show current size of nix store
    '';
}
