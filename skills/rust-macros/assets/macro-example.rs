macro_rules! vec_strs {
    ( $( $x:expr ),* ) => {
        vec![$( $x.to_string() ),*]
    };
}

fn main() {
    let v = vec_strs!["a", "b", "c"];
    println!("{:?}", v);
}
