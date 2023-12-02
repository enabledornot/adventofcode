inst = Int[]
open("input.txt") do file
    for line in eachline(file)
        if line[1:4]=="noop"
            push!(inst, 0)
        end
        if line[1:4]=="addx"
            push!(inst, 0, parse(Int,line[5:end]))
        end
    end
end
mult = 0
for multPoint in [20,60,100,140,180,220].-1
   mult+=(sum(inst[1:multPoint])+1)*(multPoint+1)
end
mult