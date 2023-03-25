i = 1
#while i < 23
#	println(i)
#	global i += 1
#end




 function f(x)
           println(@isdefined x)
           #x = 3
           #println(@isdefined x)
       end


#println(isdefined(odist, :sum) )



println(@isdefined(i), "\n", @isdefined(odist))

if @isdefined(odist) == false
	odist = 1
end

println(@isdefined(odist)) 



