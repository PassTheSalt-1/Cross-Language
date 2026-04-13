#[repr(C)] // represents the struct exactly as C would
pub struct ProcessInfo {
    pub pid: i32,
    pub uid: i32,
    pub rss_kb: i32,
}

#[repr(C)] // create a policy struct in C format
pub struct Policy {
    pub enfore_non_negative_rss: bool,
    pub normalize_uid: bool,
}

#[no_mangle]
//extern C dictates the calling convention or ABI for this function, which in this case is C.
pub extern "C" fn get_processes(
    buffer: *mut ProcessInfo,
    count: i32,
    policy: Policy,
) 

{
    let slice = unsafe {
        std::slice::from_raw_parts_mut(buffer, count as usize)

    }; //explicitly tells the compiler we know that the pointer is valid and safe.

    for i in 0..slice.len() {
        slice[i].pid = 2000 + i as i32;
        let mut uid = if i % 2 == 0 {0} else {500};
        
        let mut rss = (i as i32 + 1) * 1024; //create a mutable var to use for validation logic
        if policy.enfore_non_negative_rss && rss < 0 {
            rss = 0;
        }
        if policy.normalize_uid && uid != 0 && uid < 1000 {
            uid = 1000;
        }
        slice[i].uid = uid;
        slice[i].rss_kb = rss; // assign validated var back to our struct value
    }
}