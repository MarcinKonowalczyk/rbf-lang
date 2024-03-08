# rbf-lang

[Reversible BitFuck](https://esolangs.org/wiki/Reversible_Bitfuck) (RBF) is a [reversible Turing tarpit](https://cstheory.stackexchange.com/questions/22128/reversible-turing-tarpits) programming language. It is based on a tape of bits and has 5 commands:

 - `*` Toggle the current bit
 - `>` Shift the tape head right
 - `<` Shift the tape head left
 - `(` If the current bit is zero, jump past matching `)`
 - `)` If the current bit is zero, jump to just after matching `(`

Here is an example program operating on 3 bits. Bit 0 is the source bit (`x`), bit 1 is the target bit (`y`) and bit 2 is the temporary bit (`f`). Here the value of `x` is being moved to `y`.

```sh
# x=?, y=0, f=0
(>>*<<)        # set f if x is set
>>(            # if f is set
    <(>*<)*    # set y
    <*(>>*<<)  # unset x
>>)
<(>*<)         # if y is set, unset f
```

we can run the above program on an example tape (`100`) with rbf cli:

```sh
rbf -t "100" "(>>*<<)>>(<(>*<)*<*(>>*<<)>>)<(>*<)"  # outputs 010
```

## installation

RBF can be installed from source with

```sh
pip install .
```

or from pypi with

```sh
pip install rbf-lang
```


## links

- https://en.wikipedia.org/wiki/Toffoli_gate
- https://arxiv.org/abs/1110.2574
- https://www.sciencedirect.com/science/article/abs/pii/016727899090185R?via%3Dihub