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
sumlist = [sum(inst[1:x]) for x in 1:length(inst)]
sumlist'
map = [abs((x-1)%40-sumlist[x])<2 for x in 1:length(sumlist)]
maped = reshape(map,40,6)'
for x in 1:6
    for y in 1:40
        if maped[x,y]
            print('█')
        else
            print(' ')
        end
    end
    println("")
end