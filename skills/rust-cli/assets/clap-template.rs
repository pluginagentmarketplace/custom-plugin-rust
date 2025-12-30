use clap::Parser;

#[derive(Parser)]
#[command(name = "myapp", about = "A CLI application")]
struct Args {
    #[arg(short, long)]
    name: String,
}

fn main() {
    let args = Args::parse();
    println!("Hello, {}!", args.name);
}
